let check = setInterval(() => {
    let wrapperPicture = document.getElementById('picture').children
    console.log(wrapperPicture)
    if (wrapperPicture.length > 0) {
        clearInterval(check)
        getEmptySpaceValues()
        activeParts()
    }
}, 1000)

//get top, bottom, left and right values of empty space 

function getEmptySpaceValues() {
    let loadedPicture = document.getElementById('loadedPicture')
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