const apagar_task = (id) => {
    fetch('http://127.0.1:8000/tasks/delete/' + id, {
        method: 'GET'
    }).then((response) => {
        if (response.ok) {
            window.location.reload();
        }
    });
}

const change_status = (id) => {
    fetch('http://127.0.1:8000/tasks/change_status/' + id, {
        method: 'GET'
    }).then((response) => {
        if (response.ok) {
            window.location.reload();
        }
    });
}
