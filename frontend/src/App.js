import React from "react";
import Feed from "./components/Feed";
import Leaderboard from "./components/Leaderboard";

function App() {
  return (
    <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: "20px", padding: "20px" }}>
      <Feed />
      <Leaderboard />
    </div>
  );
}

export default App;
