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
    listEmptyValues = [widthUnit * 3, heightUnit * 3, widthUnit * 4, heightUnit * 4]
}

function countSum(arr) {
    let sum = 0
    for (let item of arr) {
        sum += item;
    }
    return sum
}

function addCursor(parent) {
    let cursor = document.createElement('div')
    cursor.classList.add('cursor')
    cursor.style.backgroundImage = "url('finger.png')"
    parent.appendChild(cursor)
}

//finding parts of the picture adjacent to empty space

function activeParts() {

    let pictureParts = document.querySelectorAll('.pictureParts')
    for (let i = 0; i < pictureParts.length; i++) {
        let left = parseInt(pictureParts[i].style.left)
        let top = parseInt(pictureParts[i].style.top)
        let listCssValues = [left, top, left + widthUnit, top + heightUnit]
        let sumEmptyValues = countSum(listEmptyValues)
        let sumCssValues = countSum(listCssValues)
        if (sumCssValues + 2 * widthUnit == sumEmptyValues || sumCssValues + 2 * heightUnit == sumEmptyValues || sumCssValues - 2 * widthUnit == sumEmptyValues || sumCssValues - 2 * heightUnit == sumEmptyValues) {
            pictureParts[i].classList.add('active')
            addCursor(pictureParts[i])
            pictureParts[i].lastChild.addEventListener('click', () => {
                changePosition(pictureParts[i], listCssValues)
                activeParts()
            })
        }
    }
}

function originalSettings() {
    let activeElements = document.querySelectorAll('.active')
    for (let i = 0; i < activeElements.length; i++) {
        activeElements[i].classList.remove('active')
        activeElements[i].removeChild(document.querySelector('.cursor'))
    }
}

function changePosition(item, valuesList) {
    originalSettings()
    item.style.left = listEmptyValues[0] + "px"
    item.style.top = listEmptyValues[1] + "px"
    listEmptyValues = valuesList
}