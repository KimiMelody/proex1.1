var headResultsButtons = document.querySelectorAll('.head_results');

// วนลูปผ่านปุ่มทั้งหมดและเพิ่มการฟังก์ชัน onClick
headResultsButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const resultsTable = button.nextElementSibling;
      const isTableHidden = resultsTable.style.display === 'none';
  
      if (isTableHidden) {
        resultsTable.style.display = 'table';
        resultsTable.classList.add('slide-down-animation');
      } else {
        resultsTable.style.display = 'none';
        resultsTable.classList.remove('slide-down-animation');
      }
    });
  });
