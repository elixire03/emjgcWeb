
 $("form#save_slider").submit(function(event){
     event.preventDefault();
     Save();
 });
 // Edit Slider form
 $("form#edit_slider").submit(function(event){
     event.preventDefault();
     if($('#edit_slider_id').val()==''){
         alert('Nothing to Edit');
         $('#edit_slider').modal('hide');
     }
     else{
         Edit();
     }
 });
 // Delete Slider Form
 $("#btn_delete").click('submit',function(event){
     event.preventDefault();
     alert('Button is Working');
     // Delete();
 });

 // ADD NEW SLIDER
 function Save(){
     var formData = new FormData();
     formData.append('slider_name', $("#slider_name").val());
     formData.append('slider_no',$('#slider_no').val());
     formData.append('contentOne',$('#contentOne').val());
     formData.append('contentTwo',$('#contentTwo').val());
     formData.append('slider_image',$('#slider_image').val());
     Image_file = document.getElementById("slider_image").files[0];
     formData.append('image_file',Image_file);
     formData.append('status',$('#status').val());
     formData.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val());
         $.ajax({
             type:'POST',
             url: '/add_slider/',
             processData: false,
             contentType:false,
             data: formData,
             beforeSend : function(){
                 
                     
                     $("#slider_name").prop('disabled', 'disabled');
                     $("#slider_no").prop('disabled', 'disabled');
                     $("#contentOne").prop('disabled', 'disabled');
                     $("#contentTwo").prop('disabled', 'disabled');
                     $("#slider_image").prop('disabled', 'disabled');
                     $("#status").prop('disabled', 'disabled');
                     $('#btn_save').prop('disabled', 'disabled');
                     $('#loading').show();
                     $('#save').hide();
                     
             },
             success : function(text){
                 if(text=='Saved')
                     
                     $("#slider_name").val('').removeAttr('disabled');
                     $("#slider_no").val('').removeAttr('disabled');
                     $("#contentOne").val('').removeAttr('disabled');
                     $("#contentTwo").val('').removeAttr('disabled');
                     $("#slider_image").val('').removeAttr('disabled');
                     $("#status").val('').removeAttr('disabled');
                     $('#btn_save').removeAttr('disabled');
                     $('#loading').hide();
                     $('#save').show();
                     List();
             }
         }); 
     }
 // EDIT AND UPDATE SLIDER
 function Edit(){
     var formData = new FormData();
     formData.append('edit_slider_id', $("#edit_slider_id").val());
     formData.append('edit_slider_name', $("#edit_slider_name").val());
     formData.append('edit_slider_no',$('#edit_slider_no').val());
     formData.append('edit_contentOne',$('#edit_contentOne').val());
     formData.append('edit_contentTwo',$('#edit_contentTwo').val());
     formData.append('edit_slider_image',$('#edit_slider_image').val());
     Image_file = document.getElementById("edit_slider_image").files[0];
     formData.append('image_file',Image_file);
     formData.append('edit_status',$('#edit_status').val());
     formData.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val());
         $.ajax({
             type:'POST',
             url: '/edit_slider/',
             processData: false,
             contentType:false,
             data: formData,
             beforeSend : function(text){
                 
                     
                     $("#edit_slider_name").prop('disabled', 'disabled');
                     $("#edit_slider_no").prop('disabled', 'disabled');
                     $("#edit_contentOne").prop('disabled', 'disabled');
                     $("#edit_contentTwo").prop('disabled', 'disabled');
                     $("#edit_slider_image").prop('disabled', 'disabled');
                     $("#edit_status").prop('disabled', 'disabled');
                     $('#btn_edit').prop('disabled', 'disabled');
                     $('#loading2').show();
                     $('#edit').hide();
                     $('#btn_delete').hide();
                     
             },
             success : function(text){
                 if(text=='Updated')
                     alert('Updated!!!');
                     
                     $('#edit_modal').modal('hide');
                     $('#edit').show();
                     $('#loading2').hide();
                     $('#delete').show();
                     List();
                     
             }
         }); 
     }

     function Delete(){
     var formData = new FormData();
     formData.append('edit_slider_id', $("#edit_slider_id").val());
     
         $.ajax({
             type:'POST',
             url: '/delete_slider/',
             processData: false,
             contentType:false,
             data: formData,
             beforeSend : function(text){
                     $('#btn_delete').prop('disabled', 'disabled');
                     $('#loading3').show();
                     $('#delete').hide();
                     
                     
             },
             success : function(text){
                 if(text=='Deleted')
                     alert('Deleted!!!');
                     
                     $('#edit_modal').show();
                     $('#loading2').hide();
                     $('#delete').show();
             }
         }); 
     }
 // DISPLAY SLIDERS
 function List(){
     var formData = new FormData();
     formData.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val());
     $.ajax({
         url:"/list_slider/",
         dataType : "html",
         success:function(text){
             // console.log(text)
             $('#display').html(text);
         }, 
     });
 }

 // Edit Button
 function Edit_slider(id,name,slider_no,title,content,status, image_name){
     $( "#edit_modal" ).modal("show");
     $("#edit_slider_id").val(id).removeAttr('disabled');
     $("#edit_slider_name").val(name).removeAttr('disabled');
     $("#edit_slider_no").val(slider_no).removeAttr('disabled');
     $("#edit_contentOne").val(title).removeAttr('disabled');
     $("#edit_contentTwo").val(content).removeAttr('disabled');
     $("#edit_slider_image").removeAttr('disabled');
     $("a[href='/media/']").attr('href', '/media/slider/'+image_name)
     $("#edit_status").val(status).removeAttr('disabled');
     $("#btn_edit").removeAttr('disabled');
     

 }
 // ADD NEW SLIDER -  
 // ENABLE BUTTON
 $( "#btn_enable" ).click(function() {
     
     $("#slider_name").removeAttr('disabled');
     $("#slider_no").removeAttr('disabled');
     $("#contentOne").removeAttr('disabled');
     $("#contentTwo").removeAttr('disabled');
     $("#slider_image").removeAttr('disabled');
     $("#status").removeAttr('disabled');
     $( "#btn_enable" ).hide();
     $( "#btn_disable" ).show();
     $("#btn_save").removeAttr('disabled');
     $("#btn_cancel").removeAttr('disabled');
     $( "#enable_module" ).modal("hide");
     $("#slider_name").focus();
 });
 // DISABLED BUTTON
 $( "#btn_disable" ).click(function() {
     
     $("#slider_name").prop('disabled', 'disabled');
     $("#slider_no").prop('disabled', 'disabled');
     $("#contentOne").prop('disabled', 'disabled');
     $("#contentTwo").prop('disabled', 'disabled');
     $("#slider_image").prop('disabled', 'disabled');
     $("#status").prop('disabled', 'disabled');
     $("#btn_save").prop('disabled', 'disabled');
     $("#btn_cancel").prop('disabled', 'disabled');
     $( "#btn_enable" ).show();
     $( "#btn_disable" ).hide();

     $( "#enable_module" ).modal("hide");
 });

