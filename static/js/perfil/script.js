document.getElementById('upload-foto').addEventListener('change', function(event) {
    const [file] = event.target.files;
    if (file) {
      const previewImg = document.getElementById('preview-img');
      previewImg.src = URL.createObjectURL(file);
    }
});