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
    sumEmptyValues = (widthUnit * 3) + (widthUnit * 4) + (heightUnit * 3) + (heightUnit * 4)
    console.log(listEmptyValues, sumEmptyValues)
}

//finding parts of the picture adjacent to empty space

// function activeParts() {

//     let pictureParts = document.getElementsByClassName('pictureParts')
//     for (let i = 0; i < pictureParts.length; i++) {
//         if (pictureParts[i].classList.contains('active')) {
//             pictureParts[i].classList.remove('active')
//         }
//         let elementId = parseInt(pictureParts[i].getAttribute('id'))
//         let widthConverter = elementId % 4
//         let heightConverter = Math.floor(elementId / 4)
//         console.log(widthConverter, heightConverter)
//         let listCssValues = [widthUnit * widthConverter, heightUnit * heightConverter, widthUnit * widthConverter + widthUnit, heightUnit * heightConverter + heightUnit]
//         pictureParts[i].style.left = listCssValues[0] + "px"
//         pictureParts[i].style.top = listCssValues[1] + "px"
//         pictureParts[i].style.right = listCssValues[2] + "px"
//         pictureParts[i].style.bottom = listCssValues[3] + "px"
//         let sumCssValues = listCssValues[0] + listCssValues[1] + listCssValues[2] + listCssValues[3]
//         if ((sumCssValues + widthUnit * 2 == sumEmptyValues) || (sumCssValues + heightUnit * 2 == sumEmptyValues)) {
//             pictureParts[i].classList.add('active')
//             pictureParts[i].addEventListener('click', () => {
//                 //changePosition(pictureParts[i], listCssValues)
//             })
//         }
//     }
// }

// function changePosition(item, valuesList) {
//     item.style.left = listEmptyValues[0] + "px"
//     item.style.top = listEmptyValues[1] + "px"
//     item.style.right = listEmptyValues[2] + "px"
//     item.style.bottom = listEmptyValues[3] + "px"
//     listEmptyValues = valuesList
//     sumEmptyValues =
// }