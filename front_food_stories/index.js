window.addEventListener('load', async function(event) {

    let response = await fetch('http://127.0.0.1:8000/api/recipes/')
    let resData = await response.json()

    let reipceList = this.document.getElementById('recipe-list')

    for (recipe of resData){
        reipceList.innerHTML += `
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <img src="${recipe.image}" class="card-img-top" alt="...">
                    <div class="card-body">
                     <p>${recipe.title}</p>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                  </div>
            </div>
        `
    }

}) 