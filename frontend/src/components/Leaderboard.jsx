import React, { useEffect, useState } from "react";

export default function Leaderboard() {
  const [leaders, setLeaders] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/leaderboard/")
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
