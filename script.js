import {projects} from "./data.js";
let list= document.getElementById('list')



projects.forEach(element => {
    var pname= element.name
    var des= element.des
    var link= 'https://realsnipc.github.io/minis/'+element.name
    var img= "https://image.thum.io/get/width/1203/crop/600/http://realsnipc.github.io/minisnips/"+element.name
    if (element.type=="py"){
        var link= 'https://github.com/realsnipc/minis/tree/main/'+element.name
        var img= 'https://www.activestate.com/wp-content/uploads/2021/12/python-coding-mistakes.jpg'
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

