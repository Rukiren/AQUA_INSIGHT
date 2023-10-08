var weather;
var title,create_element;

//抓取天氣相關資料
fetch('/static/weather.json', {
    method: 'GET',
    headers: {}
}).then((res) => {
    return res.text();   
}).then(result => {
    console.log(result);
    weather = JSON.parse(result);

    //創立元素，並分配id
    // ===========   current time   ============= //
    
    create_element = document.createElement("h3");
    create_element.setAttribute("id", "current_time_title") //給元素id
    create_element.innerHTML = "Time";
    document.getElementById("weather").appendChild(create_element); //添加至id=weather的div元素裡面

    create_element = document.createElement("p");
    create_element.setAttribute("id", "current_time") //給元素id
    create_element.innerHTML = weather.current_time;
    document.getElementById("weather").appendChild(create_element); //添加至id=weather的div元素裡面

    // ===========   probability_of_precipitation   ============= //

    create_element = document.createElement("h3");
    create_element.setAttribute("id", "probability_of_precipitation_title") //給元素id
    create_element.innerHTML = "rain probability";
    document.getElementById("weather").appendChild(create_element); //添加至id=weather的div元素裡面

    create_element = document.createElement("p");
    create_element.setAttribute("id", "probability_of_precipitation") //給元素id
    create_element.innerHTML = weather.probability_of_precipitation;
    document.getElementById("weather").appendChild(create_element); //添加至id=weather的div元素裡面

    // ===========   current time   ============= //

    create_element = document.createElement("h3");
    create_element.setAttribute("id", "weather_info_title") //給元素id
    create_element.innerHTML = "weather forecast";
    document.getElementById("weather").appendChild(create_element); //添加至id=weather的div元素裡面

    create_element = document.createElement("p");
    create_element.setAttribute("id", "weather_info") //給元素id
    create_element.innerHTML = weather.weather_info;
    document.getElementById("weather").appendChild(create_element); //添加至id=weather的div元素裡面

})

var water;


//抓取水域相關資料
fetch('/static/water.json', {
    method: 'GET',
    headers: {}
}).then((res) => {
    return res.text();   
}).then(result => {
    console.log(result);
    water = JSON.parse(result);

    //創立元素，並分配id
    // ===========   river_name   ============= //
    
    create_element = document.createElement("h3");
    create_element.setAttribute("id", "river_name_title") //給元素id
    create_element.innerHTML = "name";
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面

    create_element = document.createElement("p");
    create_element.setAttribute("id", "river_name") //給元素id
    create_element.innerHTML = water.river_name;
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面

    // ===========   pH   ============= //
    
    create_element = document.createElement("h3");
    create_element.setAttribute("id", "pH_title") //給元素id
    create_element.innerHTML = "pH";
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面

    create_element = document.createElement("p");
    create_element.setAttribute("id", "pH") //給元素id
    create_element.innerHTML = water.pH;
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面

    // ===========   water_temperature   ============= //
    
    create_element = document.createElement("h3");
    create_element.setAttribute("id", "water_temperature_title") //給元素id
    create_element.innerHTML = "Water Temperature";
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面

    create_element = document.createElement("p");
    create_element.setAttribute("id", "water_temperature") //給元素id
    create_element.innerHTML = water.water_temperature;
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面

    // ===========   pollution_level   ============= //
    
    create_element = document.createElement("h3");
    create_element.setAttribute("id", "pollution_level_title") //給元素id
    create_element.innerHTML = "PRI";
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面

    create_element = document.createElement("p");
    create_element.setAttribute("id", "pollution_level") //給元素id
    create_element.innerHTML = water.pollution_level;
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面
    
    // ===========   pollution_level_name   ============= //
    
    create_element = document.createElement("h3");
    create_element.setAttribute("id", "pollution_level_name_title") //給元素id
    create_element.innerHTML = "pollution level";
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面

    create_element = document.createElement("p");
    create_element.setAttribute("id", "pollution_level_name") //給元素id
    create_element.innerHTML = water.pollution_level_name;
    document.getElementById("water").appendChild(create_element); //添加至id=water的div元素裡面

})

var animal;


//抓取生物相關資料
fetch('/static/animal.json', {
    method: 'GET',
    headers: {}
}).then((res) => {
    return res.text();   
}).then(result => {
    console.log(result);
    animal = JSON.parse(result);

    //計算資料數量，以及給予elment id依據
    var count=0;

    //將資料根據元素id選取，依序填入
    for (i in animal) {

        var precent_div = "animal_" + count;

        //============================================//
        //!!!!底下這個 animal_number class 超重要!!!!!!//
        //============================================//

        //建立div元素，class = animal_class 內容為元素的編號
        const animal_number = document.createElement("div");
        animal_number.setAttribute("class", "animal_class") //給元素class
        animal_number.setAttribute("id", "animal_" + count) //給元素id
        document.getElementById("animal").appendChild(animal_number); //添加至id=animal的div元素裡面

        // ===========   物種名稱   ============= //

        create_element = document.createElement("h3");
        create_element.setAttribute("id", "animal_name_title") //給元素id
        create_element.innerHTML = "name";
        document.getElementById(precent_div).appendChild(create_element); //添加至id=water的div元素裡面

        //建立p元素，內容為物種名稱
        const animal_name = document.createElement("p");
        animal_name.setAttribute("id", "name_" + count) //給元素id
        animal_name.innerText = animal[i].name;
        document.getElementById(precent_div).appendChild(animal_name);

        // ===========   相片連結   ============= //

        //建立p元素，內容為相片
        const animal_photo = document.createElement("img");
        animal_photo.setAttribute("id", "photo_" + count) //給元素id
        animal_photo.setAttribute("src", animal[i].photo_link) //放入圖片超連結
        document.getElementById(precent_div).appendChild(animal_photo);

        // ===========   瀕危程度   ============= //

        create_element = document.createElement("h3");
        create_element.setAttribute("id", "danger_title") //給元素id
        create_element.innerHTML = "endangerment status";
        document.getElementById(precent_div).appendChild(create_element); //添加至id=water的div元素裡面

        //
        const danger = document.createElement("p");
        danger.setAttribute("id", "danger_" + count) //給元素id
        danger.innerHTML = animal[i].danger //放入圖片超連結
        document.getElementById(precent_div).appendChild(danger);

        // ===========   物種介紹   ============= //

        //建立div元素，class = animal_class 內容為元素的編號

        create_element = document.createElement("h3");
        create_element.setAttribute("id", "info_title") //給元素id
        create_element.innerHTML = "Info";
        document.getElementById(precent_div).appendChild(create_element); //添加至id=water的div元素裡面

        info_div = String("animal_info_" + count)

        const animal_info = document.createElement("div");
        animal_info.setAttribute("class", "info") //給元素class
        animal_info.setAttribute("id", "animal_info_" + count) //給元素id
        document.getElementById(precent_div).appendChild(animal_info); //添加至id=water的div元素裡面
        
        //建立p元素，內容為物種介紹
        for(j in animal[i].info){

            console.log([j])
            console.log(animal[i].info[j])

            //wiki簡介標題
            const title = document.createElement("h4");
            title.setAttribute("id", "title_" + count) //給元素id
            title.setAttribute("class", "title_class") //給元素class
            title.innerText = [j];
            document.getElementById(info_div).appendChild(title);

            //wiki簡介內容
            const content = document.createElement("p");
            content.setAttribute("id", "title_" + count) //給元素id
            content.setAttribute("class", "title_class") //給元素class
            content.innerText = animal[i].info[j];
            document.getElementById(info_div).appendChild(content);
        }

        //參考自 https://www.w3schools.com/jsref/met_document_createelement.asp

        count++;
        
    }

})

//document.getElementById("demo").innerHTML = obj.sites[1].name + " " + obj.sites[1].url;