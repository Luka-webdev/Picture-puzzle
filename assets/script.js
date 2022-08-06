let flag = false;
let check = setInterval(() => {
    let newImg = document.getElementById('newImg')
    if (newImg && flag == false) {
        flag = true
        getEmptySpaceValues()
        activeParts()
    }
    newImg.addEventListener('click', () => {
        flag = false
    })
}, 1500)

//get top, bottom, left and right values of empty space 

function getEmptySpaceValues() {
    let loadedPicture = document.getElementById('loadedPicture')
    let pictureWidth = parseInt(getComputedStyle(loadedPicture).width)
    let pictureHeight = parseInt(getComputedStyle(loadedPicture).height)
    widthUnit = pictureWidth / 3
    heightUnit = pictureHeight / 3
    listEmptyValues = [widthUnit * 2, heightUnit * 2, widthUnit * 3, heightUnit * 3]
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
        if ((sumCssValues + 2 * widthUnit == sumEmptyValues || sumCssValues + 2 * heightUnit == sumEmptyValues || sumCssValues - 2 * widthUnit == sumEmptyValues || sumCssValues - 2 * heightUnit == sumEmptyValues) && (Math.abs(listCssValues[0] - listEmptyValues[0]) == widthUnit || (Math.abs(listCssValues[1] - listEmptyValues[1]) == heightUnit))) {
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