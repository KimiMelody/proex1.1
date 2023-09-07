function checkInput(input) {
    if (input.value.trim() === '') {
        input.classList.add('โปรดกรอกข้อมูล');
    } else {
        input.classList.remove('โปรดกรอกข้อมูล');
    }
}