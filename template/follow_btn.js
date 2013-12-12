<script type="text/javascript">
function follow_togger(e, blog_id){
  var caller = e.target || e.srcElement;
  var $this = $(caller);
  $.ajax({
    url: "{%url 'toggle_follow_ajax'%}",
    type: "GET",
    data:{
      user_id:"{{user.id}}",
    blog_id: blog_id
    }
  }).done(function(data){
    console.log(data);
    var is_followed = data.is_followed;
    if (is_followed == 0){
      $this.data("is_followed", 0);
      <!--$this.html("Follow");-->
    setToFollow($this);
    }else{
      $this.data("is_followed", 1);
      <!--$this.html("Following");-->
    setToFollowing($this);
    }
  });
}
function setToFollowing($btn){
  $btn.html("<span class=\"glyphicon glyphicon-ok\"></span> Following");
  //$btn.attr("class","btn btn-info btn-xs");
  $btn.toggleClass("btn-info");
  $btn.toggleClass("btn-default");

}
function setToFollow($btn){
  $btn.html("Follow")
    //$btn.attr("class","btn btn-default btn-xs");
  $btn.toggleClass("btn-info");
  $btn.toggleClass("btn-default");
}
</script>
