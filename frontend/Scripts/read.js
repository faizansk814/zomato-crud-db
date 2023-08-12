const container = document.getElementById("append")

function DisplayData() {
    fetch(`https://zomatodbserverr.onrender.com/crud/get`)
        .then((res) => res.json())
        .then((data) => {
            fetchAndRender(data.data)
        })
        .catch((err) => console.log(err))
}
DisplayData()
function fetchAndRender(data) {
    container.innerHTML = ""
    data.forEach((ele) => {
        const div = document.createElement("div")
        div.classList.add("newdiv")
        let id = document.createElement("p")
        id.innerText = ` ID : ${ele.id}`
        let dishname = document.createElement('p')
        dishname.innerText = ` DISHNAME : ${ele.dishname}`
        let price = document.createElement('p')
        price.innerText = `PRICE : ${ele.price}`
        let available = document.createElement('p')
        available.innerText = `AVAILABLITY : ${ele.available}`
        let deletebutton=document.createElement('button')
        deletebutton.innerText="Delete"
        let updatebutton=document.createElement('button')
        updatebutton.innerText="Update"
        deletebutton.addEventListener('click',()=>{
            fetch(`https://zomatodbserverr.onrender.com/crud/delete/${ele.id}`,{
                method:"DELETE"
            })
            .then((res)=>{
                return res.json()
            })
            .then((data)=>{
                DisplayData()
            })
            .catch((err)=>{
                alert(err)
                console.log(err)
            })
        })
        updatebutton.addEventListener('click',()=>{
            fetch(`https://zomatodbserverr.onrender.com/crud/update/${ele.id}`,{
                method:"PATCH"
            })
            .then((res)=>{
                return res.json()
            })
            .then((data)=>{
                DisplayData()
            })
            .catch((err)=>{
                console.log(err)
            })
        })
        div.append(id, dishname, price, available,deletebutton,updatebutton)
        container.append(div)

    });

}