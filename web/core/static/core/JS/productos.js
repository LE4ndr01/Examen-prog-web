

let url = "localhost:8000/api/producto"
$.get(url,function(respuesta){
    
    respuesta.forEach(function(item){
        console.log(item)
    })

    
    

},'json')