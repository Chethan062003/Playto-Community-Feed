import React, { useEffect, useState } from "react";

export default function Leaderboard() {
  const [leaders, setLeaders] = useState([]);

  useEffect(() => {
    fetch("https://playto-community-feed-12gt.onrender.com/api/leaderboard/")
      .then(res => res.json())
      .then(data => setLeaders(data));
  }, []);

  return (
    <div className="p-4 border rounded">
      <h2 className="font-bold mb-2">Top 5 (Last 24h)</h2>
      {leaders.map((l, i) => (
        <p key={i}>
          User {l.owner} — {l.total_karma} karma
        </p>
      ))}
    </div>
  );
}
