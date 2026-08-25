// Simulating a mini social feed for now
let posts = [];
let currentUser = "Teena Mehra";

function renderFeed() {
    const feedContainer = document.getElementById("feed");
    
    if (feedContainer) {
        feedContainer.innerHTML = posts.map(post => `
            <div class="post-card">
                <div class="post-header">
                    <div class="user-info">
                        <div class="avatar">${post.user[0]}</div>
                        <span class="post-user">${post.user}</span>
                    </div>
                    <span class="post-time">Just now</span>
                </div>
                <p class="post-content">${post.content}</p>
                <div class="post-actions">
                    <button class="action-btn like-btn" onclick="likePost(this)"><i class="fa-solid fa-heart"></i> ${post.likes} Likes</button>
                    <button class="action-btn comment-btn"><i class="fa-solid fa-comment"></i> Comment</button>
                    <button class="action-btn share-btn"><i class="fa-solid fa-share"></i> Share</button>
                </div>
            </div>
        `).join("");

        // Add default post if empty
        if (posts.length === 0) {
            feedContainer.innerHTML = `
                <div class="post-card">
                    <div class="post-header">
                        <div class="user-info">
                            <div class="avatar">A</div>
                            <span class="post-user">Alpha Tech</span>
                        </div>
                        <span class="post-time">2 hours ago</span>
                    </div>
                    <p class="post-content">Just finished my Task 2 frontend! This dark navy UI looks amazing! 🚀🎉</p>
                    <div class="post-actions">
                        <button class="action-btn like-btn" onclick="likePost(this)"><i class="fa-solid fa-heart"></i> 23 Likes</button>
                        <button class="action-btn comment-btn"><i class="fa-solid fa-comment"></i> 8 Comments</button>
                        <button class="action-btn share-btn"><i class="fa-solid fa-share"></i> Share</button>
                    </div>
                </div>
            `;
        }
    }
}

function createPost() {
    const content = document.getElementById("post-content").value.trim();
    if (!content) {
        alert("Please write something!");
        return;
    }

    posts.unshift({
        user: currentUser,
        content: content,
        likes: 0
    });

    document.getElementById("post-content").value = "";
    renderFeed();
}

function likePost(button) {
    // Simple like increment logic
    const text = button.innerHTML;
    let count = parseInt(text.match(/\d+/)[0]) || 0;
    count++;
    button.innerHTML = `<i class="fa-solid fa-heart"></i> ${count} Likes`;
    button.style.color = "#e94560";
}

// Initialize
document.addEventListener("DOMContentLoaded", () => {
    const postBtn = document.getElementById("post-btn");
    if (postBtn) {
        postBtn.addEventListener("click", createPost);
    }
    renderFeed();
});