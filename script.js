import {projects} from "./data.js";
let list= document.getElementById('list')
import splt from "https://cdn.skypack.dev/spltjs@1.0.8";
import anime from "https://cdn.skypack.dev/animejs@3.2.1";

splt({
    reveal: true
  });
  
  anime({
    targets: '.reveal',
    translateY: [0, 20],
    direction: 'alternate',
    loop: 1,
    delay: anime.stagger(25),
    easing: 'cubicBezier(.71,-0.77,.43,1.67)'
  });
  
projects.forEach(element => {
    var pname= element.name
    var des= element.des
    var link= 'https://realsnipc.github.io/minis/'+element.name
    var img= "https://image.thum.io/get/width/1203/crop/600/http://realsnipc.github.io/minisnips/"+element.name
    if (element.type=="py"){
        var link= 'https://github.com/realsnipc/minis/tree/main/'+element.name
        var img= 'https://www.activestate.com/wp-content/uploads/2021/12/python-coding-mistakes.jpg'
    }
    else if (element.type=="react"){
        var link= 'https://github.com/realsnipc/minis/tree/main/'+element.name
        var img= 'https://c4.wallpaperflare.com/wallpaper/294/834/442/reactjs-facebook-javascript-minimalism-wallpaper-preview.jpg'
    }
    let template= `                <div class="p-4 md:w-1/3 sm:mb-0 mb-6">

    <!-- this is start -->
    <div class="rounded-lg h-64 overflow-hidden">
        <img alt="content" class="object-cover object-center h-full w-full  border-4 rounded"
            src="${img}">
    </div>
    <h2 class="text-xl font-medium title-font text-gray-900 mt-5">${pname}</h2>
    <p class="text-base leading-relaxed mt-2">${des}</p>
    <a class="text-indigo-500 inline-flex items-center mt-3" href="${link}">Visit
        <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
            stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
        </svg>
    </a>
    <!-- this is end -->
</div>`
console.log("im running")
list.innerHTML += template
})

