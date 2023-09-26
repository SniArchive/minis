let input_tag= document.getElementById('input')
let add_tag= document.querySelector('button')
let list_tag= document.querySelector('.list-group')
var taskarray=[]

let fetched_tasks= localStorage.getItem('task')
if (fetched_tasks!=null){
 taskarray= JSON.parse(fetched_tasks)}
displaytask()


function add_tag_event(){
    add_tag.addEventListener('click',()=>{
        addtask(input_tag.value)
    })
  }

function addtask(input_passed){
    taskarray.push(input_passed)
    localStorage.setItem('task',JSON.stringify(taskarray))
    location.reload();
}
function displaytask(){
    var i=0
    taskarray.forEach(element => {
        var i= i+1
        let text= `<button type="button" class="list-group-item list-group-item-action" onclick='removetask(${i})'>${element}</button>`
        list_tag.innerHTML += text
    });


}
function removetask(item_id){
    taskarray.splice(item_id,1)
    localStorage.setItem('task',JSON.stringify(taskarray))
    location.reload()
}

add_tag_event()


