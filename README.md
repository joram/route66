# Route66

this project is designed to look at docker labels and create a simple grid of image links to all the services.

## Usage (with traefik)
```yaml
  route66:
    image: joram87/route66:latest
    container_name: route66
    restart: unless-stopped
    labels:
      - traefik.enable=true
      - traefik.http.routers.route66.rule=Host(`<url>`)
      - traefik.http.routers.route66.tls=true
      - traefik.http.services.route66.loadbalancer.server.port=80
      - route66.image.url=https://cdn.worldvectorlogo.com/logos/route-66-1.svg
      - route66.group=Infrastructure
    depends_on:
      - traefik
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
```

and then all other docker containers you wish to be accessible should have the following

### Http Rule
`traefik.http.routers.<name>.rule`

this tag will have the `Host('<url>')` value pulled out and be where the service will be linked to.

### Image Url
`route66.image.url`

this tag will have the url to the image you wish to use for the link.

### Group
`route66.group`

this tag will be used to group the links together. if you have multiple services with the same group name they will be grouped together.

### Enable
`route66.enable`

this tag will enable or disable the link from being displayed. if this tag is not present it will default to disabled.
