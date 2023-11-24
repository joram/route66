const jsonUrl = '/services';

function createServiceElement(service) {
    const imageItem = document.createElement('div');
    imageItem.classList.add('image-item');

    const imageLink = document.createElement('a');
    imageLink.href = service.url;
    imageLink.classList.add('image-link');

    const image = document.createElement('img');
    image.src = service.image_url;
    image.title = service.name;
    image.classList.add('image');

    const overlay = document.createElement('div');
    overlay.classList.add('overlay');
    overlay.textContent = service.description;

    // Append elements to the DOM
    imageLink.appendChild(image);
    imageItem.appendChild(imageLink);
    imageItem.appendChild(overlay);
    return imageItem;
}

function render() {
    fetch(jsonUrl)
        .then(response => response.json())
        .then(data => {
            const root = document.getElementById('ListOfImageGrids');
            Object.keys(data).forEach(groupName => {
                const header = document.createElement('header');
                const gridTitle = document.createElement('h1');
                gridTitle.textContent = groupName;
                header.appendChild(gridTitle);
                root.appendChild(header);

                const imageGrid = document.createElement('imageGrid');
                imageGrid.classList.add('image-grid');
                data[groupName].forEach(service => {
                    const imageItem = createServiceElement(service);
                    imageGrid.appendChild(imageItem);
                })
                root.appendChild(imageGrid);
            });
        })
        .catch(error => console.error('Error fetching JSON:', error));
}