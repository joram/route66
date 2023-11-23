#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import docker
from typing import TypedDict


class DockerServiceDetails(TypedDict):
    name: str
    traefik_enabled: bool
    traefik_rule: str
    url: str
    image_url: str
    cache_image: bool


def get_services():

    client = docker.from_env()

    grouped_services = {}

    # List Containers
    for container in client.containers.list():
        labels = container.attrs["Config"]["Labels"]
        traefik_enabled = labels.get("traefik.enable", "false").lower() == "true"
        compose_service_name = labels.get("com.docker.compose.service", None)
        traefik_rule = labels.get(f"traefik.http.routers.{compose_service_name}.rule", None)
        image_url = labels.get("route66.image.url", None)
        group = labels.get("route66.group", None)
        cache_image = labels.get("route66.image.cache", "true").lower() == "true"

        url = None
        if traefik_rule:
            url = "https://"+traefik_rule.replace("Host(`", "").replace("`)", "")

        service = DockerServiceDetails(
            name=container.name,
            traefik_enabled=traefik_enabled,
            traefik_rule=traefik_rule,
            url=url,
            image_url=image_url,
            cache_image=cache_image,
        )

        if group not in grouped_services:
            grouped_services[group] = []
        grouped_services[group].append(service)

    return grouped_services


if __name__ == "__main__":
    print(get_services())