import React from "react";

export default function Comment({ comment }) {
  return (
    <div className="mt-3 border-l pl-3">
      <p>{comment.content}</p>
      <p className="text-sm">Likes: {comment.like_count}</p>

      {comment.replies.map(r => (
        <Comment key={r.id} comment={r} />
      ))}
    </div>
  );
}
