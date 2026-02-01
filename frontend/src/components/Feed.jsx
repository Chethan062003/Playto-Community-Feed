import React, { useEffect, useState } from "react";
import Comment from "./Comment";

export default function Feed() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
   fetch("https://playto-community-feed-pdo8.onrender.com/api/feed/")
      .then(res => res.json())
      .then(data => setPosts(data));
  }, []);

  return (
    <div className="p-6">
      {posts.map(post => (
        <div key={post.id} className="border p-4 mb-6 rounded">
          <p className="font-semibold text-lg">{post.content}</p>
          <p>Likes: {post.like_count}</p>

          <div className="ml-6 mt-4">
            {post.comments.map(c => (
              <Comment key={c.id} comment={c} />
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
