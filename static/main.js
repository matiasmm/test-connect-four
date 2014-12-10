function Game(baseUrl, user_id, $table, $){
    var turn,
        data = [],
        $container = $($table.find('tbody')),
        interval;

    function main (){
        get_status();
        refresh_turn(false);
    }

    /**
     * Add an element
     * @param col
     */
    function click (col){
        var r;

        for(r = data.length-1; r >= 0; r--) {
            if (data[r][col] == null) {
                data[r][col] = user_id;
                update(r, col);
                draw();
                refresh_turn(false);
                alert('Waiting for the other player');
                break;
            }
        }
    }

    function refresh_turn(v){
        turn = v;
        if (turn) {
            $table.find('thead button').removeAttr('disabled');
        }else{
            $($table.find('thead button')).attr('disabled','disabled');
            interval = setInterval(get_status, 200);
        }
    }

    function draw(){
        var r, c, $tr, $td, $el, clss;
        $container.html('');
        for(r = data.length-1; r >= 0; r--) {
            $tr = $('<tr>').attr('row', r);
            for(c = data[r].length-1; c >= 0; c--) {
                $el = $('<div class="circle">').attr('col', c).attr('row', r);
                $td = $('<td>').append($el);
                $tr.prepend($td);

                if(data[r][c]){
                    clss = 'p' + data[r][c];
                    $el.addClass(clss);
                }
            }
            $container.prepend($tr);
        }
    }

    function get_status(){
        $.ajax({'url': baseUrl + 'api/status',
            success: function(resp) {
                data = resp.table;
                draw();

                if(resp.ended != null) {
                    if(resp.ended == user_id) {
                        alert('You Won!!!!');
                    } else {
                        alert('You Lost my friend!!!!');
                    }
                    clearInterval(interval);
                }else {
                    if(resp.turn == user_id) {
                        refresh_turn(true);
                        clearInterval(interval);
                    }
                }
            }
        })
    }

    function update(row, col){
        $.ajax({'url': baseUrl + 'api/update',
            'method': 'post',
            'data': {'row': row, 'col': col, 'player_id': user_id}
        });
    }

    main();

    this.click = click;
    this.draw = draw;
    this.data = data;
}