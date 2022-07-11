let check = setInterval(() => {
    let loadedPicture = document.getElementById('picture').children
    console.log(loadedPicture)
    if (loadedPicture.length > 0) {
        clearInterval(check)
        console.log('ok')
    }
}, 1000)