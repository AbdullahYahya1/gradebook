function getToken(name){
    const value = `; ${document.cookie}`  
    const parts = value.split(`; ${name}=`)
    if(parts.length == 2)
        return parts.pop().split(';').shift();
}

  

function deleteRoom(room_id){
    popout(room_id);
}
function popout(room_id){
    document.querySelector(`#room${room_id}`).style.display = 'block';
}
function dontDeleteRoom(room_id){
    document.querySelector(`#room${room_id}`).style.display = 'none';
}
function del(room_id){
    const csrfToken = getToken('csrftoken');
    fetch(`/deleteRoom/${room_id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,},
            body: JSON.stringify({
                class_room_id: room_id,
            }),
        }).then(response => response.json())
        .then(data => {

            if(data['status']=='good'){
                document.querySelector('.apiStat').innerHTML ="<h3>class room Deleted</h3>"
                console.log('here')
            }
             
        }).catch(error => {
            console.error('Error:', error);
        });
        dontDeleteRoom(room_id)
        classRoomA = document.querySelector(`.classRoomA${room_id}`)
        classRoomA.parentElement.removeChild(classRoomA)

}

function downloadImage() {
    const imageData = document.querySelector('img').src.split(',')[1];
    const link = document.createElement('a');
    link.href = 'data:image/png;base64,' + imageData;
    link.download = 'grade_distribution.png';
    link.click();
  }