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
    listEmptyValues = [widthUnit * 3, widthUnit * 4, heightUnit * 3, heightUnit * 4]
}

//finding parts of the picture adjacent to empty space

function activeParts() {
    let pictureParts = document.getElementsByClassName('pictureParts')
    console.log(pictureParts[0].style.order)

}