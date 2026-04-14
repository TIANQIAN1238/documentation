import React from "react";

export default function EditThisPageWrapper() {
  const feedbackStyle = {
    marginTop: "20px",
    padding: "10px 15px",

    borderRadius: "8px",
    borderLeft: "4px solid #007bff", // A blue accent to match the button
    display: "flex",
    flexDirection: "column",
    alignItems: "flex-start",
  };

  return (
    <>
      <div style={feedbackStyle}>
          <p style={{ margin: 0, fontWeight: "500" }}>帮助我们把 Temporal 做得更好。欢迎为我们的 <a href="https://github.com/temporalio/documentation">文档</a> 做出贡献。</p>
      </div>
    </>
  );
}
