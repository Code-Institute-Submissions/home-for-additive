//Add elements to the renderred 'new_proposal' form 
document.getElementById('id_title').insertAdjacentHTML('afterend', '<hr>');
document.getElementById('id_title').insertAdjacentHTML('afterend', '<br>');
document.getElementById('id_keywords').insertAdjacentHTML('afterend', '<hr>');
document.getElementById('id_keywords').insertAdjacentHTML('afterend', '<br>');
document.getElementById('id_email').insertAdjacentHTML('afterend', '<hr>');
document.getElementById('id_email').insertAdjacentHTML('afterend', '<br>');
document.getElementById('id_student').insertAdjacentHTML('afterend', '<hr>');
document.getElementById('id_student').insertAdjacentHTML('afterend', '<br>');
document.getElementById('id_content').insertAdjacentHTML('afterend', '<hr>');
document.getElementById('id_content').insertAdjacentHTML('afterend', '<br>');
document.getElementById('div_id_slug').hidden = true;

console.log('the value:', document.getElementById('id_slug').value);
/*
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");


for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

*/



