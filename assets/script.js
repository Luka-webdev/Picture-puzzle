let check = setInterval(() => {
    let wrapperPicture = document.getElementById('picture').children
    console.log(wrapperPicture)
    if (wrapperPicture.length > 0) {
        clearInterval(check)
        getEmptySpaceValues()
        createEmptyBox()
        activeParts()
    }
}, 1000)

// add to picture parts empty box

function createEmptyBox() {
    emptyBox = document.createElement('div')
    emptyBox.style.width = widthUnit + "px"
    emptyBox.style.height = heightUnit + "px"
    emptyBox.style.top = (heightUnit * 3) + "px"
    emptyBox.style.left = (widthUnit * 3) + "px"
    emptyBox.style.order = 15
    loadedPicture.appendChild(emptyBox)
}

//get top, bottom, left and right values of empty space 

function getEmptySpaceValues() {
    loadedPicture = document.getElementById('loadedPicture')
    let pictureWidth = parseInt(getComputedStyle(loadedPicture).width)
    let pictureHeight = parseInt(getComputedStyle(loadedPicture).height)
    widthUnit = pictureWidth / 4
    heightUnit = pictureHeight / 4
    //listEmptyValues = [widthUnit * 3, heightUnit * 3,widthUnit * 4, heightUnit * 4]
    listEmptyValues = (widthUnit * 3) + (widthUnit * 4) + (heightUnit * 3) + (heightUnit * 4)

    console.log(listEmptyValues, widthUnit, heightUnit)
}

//finding parts of the picture adjacent to empty space

function activeParts() {

    let pictureParts = document.getElementsByClassName('pictureParts')
    let counter = 0;
    for (let i = 0; i < pictureParts.length; i++) {
        let elementId = parseInt(pictureParts[i].getAttribute('id'))
        let widthConverter = elementId % 4
        let heightConverter = Math.floor(elementId / 4)
        //let listCssValues = [widthUnit * widthConverter, heightUnit * heightConverter, widthUnit * widthConverter + widthUnit, heightUnit * heightConverter + heightUnit]
        let listCssValues = (widthUnit * widthConverter) + (heightUnit * heightConverter) + (widthUnit * widthConverter + widthUnit) + (heightUnit * heightConverter + heightUnit)
        console.log(i, listCssValues)
        if ((listCssValues + widthUnit * 2 == listEmptyValues) || (listCssValues + heightUnit * 2 == listEmptyValues)) {
            pictureParts[i].classList.add('active')
        }
    }
}