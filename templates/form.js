import React, { useState } from "react";
import axios from "axios";

function UploadVideo() {
  const [video, setVideo] = useState("");
  const [subtitle, setSubtitle] = useState("");
  const [fontSize, setFontSize] = useState("");
  const [fontName, setFontName] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("video", video);
    formData.append("srt", subtitle);
    formData.append("font_size", fontSize);
    formData.append("font_name", fontName);

    try {
      const response = await axios.post("/caption", formData);
      // Handle success
      console.log(response);
    } catch (error) {
      // Handle error
      console.log(error);
    }
  };

  return (
    <div className="upload-video">
      <h1>Upload a Video</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          onChange={(e) => setVideo(e.target.files[0])}
          accept="video/*"
        />
        <input
          type="file"
          onChange={(e) => setSubtitle(e.target.files[0])}
          accept=".srt"
        />
        <input
          type="number"
          placeholder="Font Size"
          value={fontSize}
          onChange={(e) => setFontSize(e.target.value)}
        />
        <input
          type="text"
          placeholder="Font Name"
          value={fontName}
          onChange={(e) => setFontName(e.target.value)}
        />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default UploadVideo;
