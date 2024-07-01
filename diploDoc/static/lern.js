// addlearn - класс куда необходимо добавить поле для материала

function formLern(e){e.preventDefault()}
let count = 0
let list = ['start']



function learn(type){
    count++
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
    list.push(type)
    
}


function saveform(){

    let formData = new FormData();
		formData.append( 'title' , $("#title")[0].files[0]);
        formData.append('slug' , $("#slug").val())
        formData.append('name' , $("#name").val())
        formData.append('attributes' , $("#attributes").val())
        formData.append('list' , list)
    for(; count; count--){
        if (list[count] == 'text'){
            formData.append(String(count) , $(`#${count}`).val())
        }
        else{ formData.append(String(count) , $(`#${count}`)[0].files[0])}
    }

    $.ajax({
        url: '/savelern/',
        type: "POST",
        cache: false,
        contentType: false,
        processData: false,
        data:  formData,
        dataType : 'json',

        success: function (data) {
            window.location.href = '/cms/ed_materials/'
        },
        error: function (s) {
            console.log('err');
        }
    })
    
}