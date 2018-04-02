/*
	参数解释：
	title	标题
	url		请求的url
	id		需要操作的数据id
	w		弹出层宽度（缺省调默认值）
	h		弹出层高度（缺省调默认值）
*/

/*管理员-权限-添加*/
function admin_permission_add(title, url, w, h) {
    layer_show(title, url, w, h);
}

/*管理员-权限-编辑*/
function admin_permission_edit(title, url, w, h) {
    layer_show(title, url, w, h);
}

/*管理员-权限-删除
* 参数解释：obj:删除的对象
* url:ajax提交的url
* */
function system_permission_del(obj, url) {
    $.ajax({
        type: 'POST',
        url: url,
        dataType: 'json',
        success: function (result) {
            if (result.status === 1) {
                $(obj).parents("tr").remove();
                layer.msg(result.data, {icon: 1, time: 1000});
            } else {
                layer.msg(result.data, {icon: 5, time: 1000});
            }
        }
    });
}