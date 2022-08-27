// remove welcome screen

let startGame = setTimeout(() => {
    let startBtn = document.getElementById('link')
    let welcomeScreen = document.getElementById('welcomeScreen')
    let setDimension = document.getElementById('setDimension')
    let closeArrow = document.getElementById('closeArrow')
    loadArea = document.getElementById('loadArea')
    fail = document.getElementById('#fail')
    closeArrow.addEventListener('click', () => {
        welcomeScreen.style.visibility = 'hidden'
    })
    startBtn.addEventListener('click', () => {
        setDimension.style.visibility = 'hidden'
        startVerification()
    })
}, 2000)

// start the image load recognition

function startVerification() {
    check = setInterval(verification, 1500)
}

// stop the image load recognition

function stopVerification() {
    clearInterval(check)
}

// image load recognition

function verification() {
    try {
        let newImg = document.getElementById('newImg')
        if (newImg) {
            loadArea.style.visibility = 'hidden'
            stopVerification()
            getEmptySpaceValues()
            activeParts()
            let cursors = document.getElementsByClassName('cursor')
            setTimeout(() => {
                if (cursors.length == 0) {
                    fail.style.visibility = 'visible'
                }
            }, 3000)
            newImg.addEventListener('click', () => {
                loadArea.style.visibility = 'visible'
                startVerification()
            })
        }
    } catch {
        fail.style.visibility = 'visible'
    }
}

//get top, bottom, left and right values of empty space 

function getEmptySpaceValues() {
    let loadedPicture = document.getElementById('loadedPicture')
    let pictureWidth = parseInt(getComputedStyle(loadedPicture).width)
    let pictureHeight = parseInt(getComputedStyle(loadedPicture).height)
    widthUnit = pictureWidth / 3
    heightUnit = pictureHeight / 3
    listEmptyValues = [widthUnit * 2, heightUnit * 2, widthUnit * 3, heightUnit * 3]
}

// function to count sum used to find the active parts of an image

function countSum(arr) {
    let sum = 0
    for (let item of arr) {
        sum += item;
    }
    return sum
}

//add an icon to the active parts of the image

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

// restore the original settings of the active elements after clicking on any of them

function originalSettings() {
    let activeElements = document.querySelectorAll('.active')
    for (let i = 0; i < activeElements.length; i++) {
        activeElements[i].classList.remove('active')
        activeElements[i].removeChild(document.querySelector('.cursor'))
    }
}

// change the position of the clicked element of image

function changePosition(item, valuesList) {
    originalSettings()
    item.style.left = listEmptyValues[0] + "px"
    item.style.top = listEmptyValues[1] + "px"
    listEmptyValues = valuesList
}