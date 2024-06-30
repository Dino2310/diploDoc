// addlearn - класс куда необходимо добавить поле для материала

function formLern(e){e.preventDefault()}
let count = 1
let list = ['start']



function learn(type){
    let img_in = `<div class="field">
            <div class="file">
                <label class="file-label">
                    <input id = "${count}" class="file-input" type="file"/>
                    <span class="file-cta">
                        <span class="file-label"> Выберите фото</span>
                    </span>
                </label>
            </div>
        </div>`

    let text_in = ` <div class="field">
                    <textarea id = "${count}" class="textarea"placeholder="Введите текст" ></textarea>
                </div>`
    $('.addlearn').append(type == 'text'?text_in:img_in)
    list.append[type]
    count++
}


function saveform(){



    data = { 'slug' : $("#slug").val(),
            'name' : $("#name").val(),
            'attributes' : $("#attributes").val(),
            'title' : $("#title").files,
            'titleF' : $("#title").val(),
            }
    
    for(; count-1; count--){
        if (list[count] == text){
        data[String(count)] = $(`#${count}`).val()}
        else{ data[String(count)] = $(`#${count}`).files}
        console.log(data)
    }
    $.ajax({
        url: '/savelern/',
        type: "POST",
        data: data,

        success: function (data) {
            console.log("отправлено")
        },
        error: function (s) {
            console.log('err');
        }
    })
    
}