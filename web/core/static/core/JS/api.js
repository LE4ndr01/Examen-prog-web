function initMap(){
    const ubicacion = new Mapa(()=>{
        const options = {
            center: {
                lat: -33.6011879, 
                lng: -70.5803857
            },
            
            zoom: 15
        }
        var map = document.getElementById('map');

        const mapa = new google.maps.Map(map, options);
        const marker = new google.maps.Marker({
            position: center, map:map, title: 'Mi ubicación'
                
            
        });

    });
}