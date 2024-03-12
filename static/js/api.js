



var count=0
async function Data(){
    let response= await fetch("https://fakestoreapi.com/products")
    let data=await response.json()
    
    data.forEach(
        (e)=>{
            let maindiv=document.querySelector(".container3")
            let div =document.createElement("div")
            let img =document.createElement("img")
            let imgdiv=document.createElement("div")
            let h1=document.createElement("p")
            let p=document.createElement("p")
            let button1=document.createElement("button")
            let button2=document.createElement("button")
            let b_div=document.createElement("div")
            let notify=document.querySelector(".notify")
            let notid2fy=document.querySelector("#id2")
            b_div.append(button1,button2)
            maindiv.appendChild(div)
            imgdiv.appendChild(img)
            div.append(imgdiv,h1,p,b_div)
            
            /*----------css--------------*/
            

            div.className="product"
            imgdiv.className="img_div"
            b_div.className="b-div"
            button1.className="button1"
            button2.className="button2"
            p.className="price"
            h1.className="title"
            /*-----------events-----*/
            button1.addEventListener("click",(e)=>{
                
                if( e.target.innerText=="Add To Cart"){
                    e.target.innerText="Remove From Cart"
                    e.target.style.backgroundColor="green"
                    count=count+1
                    id2.innerText=count
                    
                   
                    
                    
                    
                    
                    if (count!=0){
                        notify.style.display="block"

                    }else{
                        notify.style.display="none"

                    }
                   

                }else{
                    e.target.innerText="Add To Cart"
                    e.target.style.backgroundColor="rgb(255, 208, 0)"
                    count=count-1
                    id2.innerText=count
                    
                    
                    
                    if (count !=0){
                        notify.style.display="block"
                        

                    }else{
                        notify.style.display="none"

                    }

                    
                    
                    
                    

                }
                

               
               
                
            })


            



            /*-------values----------*/
            img.src=e.image
            h1.innerText=e.title
            p.innerText="$"+e.price
            button1.innerText="Add To Cart"
            button2.innerText="Buy"
           

        }
    )



}
window.addEventListener("DOMContentLoaded",Data)
function Cart(e){
    console.log(e.target)

}

