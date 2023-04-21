window.addEventListener("load", solve);

function solve() {
    const inputs = {
        titleEl: document.getElementById('task-title'),
        categoryEl: document.getElementById('task-category'),
        contentEl: document.getElementById('task-content')
    }
    const publishBtn = document.getElementById('publish-btn');
    publishBtn.addEventListener('click', onPublish);
    
    let ulReviewList = document.getElementById('review-list');
    let ulPublishedList = document.getElementById('published-list');
    let data = {};

    function onPublish() {
        data = {
            title: inputs.titleEl.value,
            category: inputs.categoryEl.value,
            content: inputs.contentEl.value
        }

        if (!data.title || !data.category || !data.content) {
            return
        }
        let li = document.createElement('li');
        li.className = 'rpost';
        let article = document.createElement('article');
        let h4 = document.createElement('h4');
        h4.textContent = data.title;
        let pCategory = document.createElement('p');
        pCategory.textContent = `Category: ${data.category}`;
        let pContent = document.createElement('p');
        pContent.textContent = `Content: ${data.content}`;
        let editBtn = document.createElement('button');
        editBtn.textContent = 'Edit';
        editBtn.setAttribute('class', 'action-btn edit');
        editBtn.addEventListener('click', onEdit);
        let postBtn = document.createElement('button');
        postBtn.textContent = 'Post';
        postBtn.setAttribute('class', 'action-btn post');
        postBtn.addEventListener('click', onPost);

        li.appendChild(article);
        li.appendChild(editBtn);
        li.appendChild(postBtn)
        
        article.appendChild(h4);
        article.appendChild(pCategory);
        article.appendChild(pContent);
        ulReviewList.appendChild(li);

        inputs.titleEl.value = '';
        inputs.categoryEl.value = '';
        inputs.contentEl.value = '';
    }

    function onEdit(e) {
        inputs.titleEl.value = data.title;
        inputs.categoryEl.value = data.category;
        inputs.contentEl.value = data.content;
        e.target.parentNode.remove();
    }

    function onPost(e) {
        ulPublishedList.appendChild(this.parentNode);
        e.target.parentNode.querySelector('.edit').remove();
        e.target.parentNode.querySelector('.post').remove();
    }
}
