window.addEventListener("load", solve);

// В джъдж се събмитва само функцията solve()

function solve() {
  const titleEl = document.getElementById('post-title');
  const categoryEl = document.getElementById('post-category');
  const contentEl = document.getElementById('post-content');
  const publishBtn = document.getElementById('publish-btn');
  publishBtn.addEventListener('click', onPublish);
  const ul = document.getElementById('review-list'); 

  function onPublish() {
      let title = titleEl.value;
      let category = categoryEl.value;
      let content = contentEl.value;

      if (!title || !category || !content) {
        return;
      }

      let li = document.createElement('li');
      li.className = 'rpost';
      li.innerHTML = `<article>
                        <h4>${title}</h4>
                        <p>Category: ${category}</p>
                        <p>Content: ${content}</p>
                      </article>
                      <button class="action-btn edit">Edit</button>
                      <button class="action-btn approve">Approve</button>`;

      ul.appendChild(li);

      titleEl.value = '';
      categoryEl.value = '';
      contentEl.value = '';

      let editBtn = document.querySelector('.edit');
      editBtn.addEventListener('click', onEdit);
      let approveBtn = document.querySelector('.approve');
      approveBtn.addEventListener('click', onApprove);

      function onEdit(event) {
        titleEl.value = title;
        categoryEl.value = category;
        contentEl.value = content;

        event.target.parentNode.remove();
      }

      function onApprove() {
        let ulPublished = document.getElementById('published-list');
        ulPublished.innerHTML = ul.innerHTML;
        ul.innerHTML = '';
        document.querySelector('.edit').remove();
        document.querySelector('.approve').remove();
      }

      let clearBtn = document.getElementById('clear-btn');
      clearBtn.addEventListener('click', onClear);

      function onClear() {
        document.getElementById('published-list').innerHTML = '';
      }
  }
}
