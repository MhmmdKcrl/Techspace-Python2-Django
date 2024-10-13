window.addEventListener('load', async function(event) {
    let responseCats = await fetch('http://127.0.0.1:8000/api/cats/')
    let catsData = await responseCats.json()
    let catSelect = this.document.getElementById('category-list')
    for (cat of catsData){
        catSelect.innerHTML += `
        <option value="${cat.id}">${cat.name}</option>
        `
    }

    let responseTags = await fetch('http://127.0.0.1:8000/api/tags/')
    let tagsData = await responseTags.json()
    let tagsSelect = this.document.getElementById('tag-list')
    for (tag of  tagsData){
        tagsSelect.innerHTML += `
        <option value="${tag.id}">${tag.name}</option>
        `
    }

})

let accessToken = localStorage.getItem('token')
let form = document.getElementById('create-form')
form.addEventListener('submit', async function(event){
    event.preventDefault()
    
    let newform = new FormData(form)

    let response = await fetch('http://127.0.0.1:8000/api/recipes/',
        {
        method: "POST",
        headers:{
        'Authorization': `Bearer ${accessToken}`,
        },
        body: newform

    })
})