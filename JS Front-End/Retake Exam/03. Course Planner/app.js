let BASE_URL = 'http://localhost:3030/jsonstore/tasks/';

const loadCoursesBtn = document.getElementById('load-course');
loadCoursesBtn.addEventListener('click', onLoad);
const listCourses = document.getElementById('list');
const addBtn = document.getElementById('add-course');
addBtn.addEventListener('click', onAdd);
const editCourseBtn = document.getElementById('edit-course');
editCourseBtn.addEventListener('click', onEditCourse);

const courseTitleEl = document.getElementById('course-name');
const courseTypeEl = document.getElementById('course-type');
const descriptionEl = document.getElementById('description');
const teachersNameEl = document.getElementById('teacher-name');
let id = null;

function onLoad() {
    fetch(BASE_URL)
        .then((response) => response.json())
        .then((data) =>  { 
            listCourses.innerHTML = '';

            for (let info of Object.values(data)) {
                id = info._id;
                let div = document.createElement('div');
                div.className = 'container';
                let h2 = document.createElement('h2');
                h2.textContent = info.title;
                let h3Name = document.createElement('h3');
                h3Name.textContent = info.teacher;
                let h3Type = document.createElement('h3');
                h3Type.textContent = info.type;
                let h4 = document.createElement('h4');
                h4.textContent = info.description;
                let editBtn = document.createElement('button');
                editBtn.setAttribute('class', 'edit-btn');
                editBtn.id = id
                editBtn.textContent = 'Edit Course';
                editBtn.addEventListener('click', onEdit);
                let finishBtn = document.createElement('button');
                finishBtn.id = id;
                finishBtn.setAttribute('class', `finish-btn`);
                finishBtn.textContent = 'Finish Course';
                finishBtn.addEventListener('click', onFinish);
            
                div.appendChild(h2);
                div.appendChild(h3Name);
                div.appendChild(h3Type);
                div.appendChild(h4);
                div.appendChild(editBtn);
                div.appendChild(finishBtn);
                listCourses.appendChild(div);
            }
         });
        editCourseBtn.disabled = true;
   }

   function onAdd(e) {
    e.preventDefault();
        let courseTitle = courseTitleEl.value;
        let courseType = courseTypeEl.value;
        let description = descriptionEl.value;
        let teacherName = teachersNameEl.value;
       fetch(BASE_URL, {
        method: 'POST',
        body: JSON.stringify({
                "title": courseTitle,
                "type": courseType,
                "description": description,
                "teacher": teacherName
            })
       })
       .then(() => onLoad());

       clear();
       editBtn.disabled = true;
       addBtn.disabled = false;
   }

   function onEdit(e) {
    e.preventDefault();
    id = e.target.id;
    courseTitleEl.value = e.target.parentNode.querySelector('h2').textContent;
    courseTypeEl.value = e.target.parentNode.querySelector('h3:nth-child(3)').textContent;
    descriptionEl.value = e.target.parentNode.querySelector('h4').textContent;
    teachersNameEl.value = e.target.parentNode.querySelector('h3:nth-child(2)').textContent;
    e.target.parentNode.remove();
    editCourseBtn.disabled = false;
    addBtn.disabled = true;
    
   }

   function onEditCourse(e) {
    e.preventDefault();
    let title = courseTitleEl.value;
    let type = courseTypeEl.value;
    let description = descriptionEl.value;
    let teacher = teachersNameEl.value;

    fetch(BASE_URL + id, {
        method: 'PATCH',
        body: JSON.stringify({ title, type, description, teacher })
    })
    .then(() => onLoad());
     clear();
   }

   function onFinish(e) {
    id = e.target.id;
    fetch(BASE_URL + id, {
        method: 'DELETE',
    })
    .then(() => onLoad());

   }

   function clear() {
       courseTitleEl.value = '';
       courseTypeEl.value = '';
       descriptionEl.value = '';
       teachersNameEl.value = '';
   }
