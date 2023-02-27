function songs(songsData) {
    let n = songsData.shift();
    let typeSong = songsData.pop();

    let songsList = [];

    for(let song of songsData) {
        song = song.split('_');

        if (typeSong == 'all') {
            songsList.push(song[1]);
        } else if (song[0] == typeSong) {
            songsList.push(song[1]);
        }
       
    }
    console.log(songsList.join('\n'));
}
