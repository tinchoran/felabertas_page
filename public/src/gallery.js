const cover = document.querySelector(".carousel__cover");
const images = document.querySelectorAll(".carousel__cover-img");
const botones = document.querySelectorAll(".carousel__btn")
const markers = document.querySelectorAll(".carousel__ubi-item")
const figCaption = document.querySelector(".carousel__figcaption")
const anios = [2020, 2019, 2021, 2021, 2021]


//Contador
let counter = 0;

//Pasar a la siguiente foto
const siguiente  = async (cont)=>{
    images[cont - 1].style.clipPath = "inset(0 100% 0 0)";
    images[cont].style.clipPath = "inset(0 0 0 0)"
    figCaption.innerHTML = `${anios[cont]}`
}


//Volver a la foto anterior
const anterior = (cont)=>{
    images[cont + 1].style.clipPath = "inset(0 0 0 100%)";
    images[cont].style.clipPath = "inset(0 0 0 0)";
    figCaption.innerHTML = `${anios[cont]}`
}

//Marcar el rectangulo que indica la foto actual
let auxcontMax = 0
const mark  = (cont)=>{
    markers.forEach(m => m.style.backgroundColor = "grey")
    markers[cont].style.backgroundColor = "white";
    //Poner el primer año
    figCaption.innerHTML = `${anios[cont]}`
    return auxcontMax = cont;
}

//Slider
botones.forEach(btn =>{
    btn.addEventListener("click", (e)=>{
        if(e.target.id === "carousel__btnRight"){
            if(counter < 4){
                counter += 1
                mark(counter)
                siguiente(counter)
            }
        }
        else if(e.target.id === "carousel__btnLeft"){
            if(counter > 0){
                counter -= 1
                mark(counter)
                anterior(counter)
            }
        }
    })
})

//Marcar el primer rectángulo al comienzo
window.onload = function(){mark(0)}
