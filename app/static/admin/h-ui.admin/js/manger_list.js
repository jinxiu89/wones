/*
	参数解释：
	title	标题
	url		请求的url
	id		需要操作的数据id
	w		弹出层宽度（缺省调默认值）
	h		弹出层高度（缺省调默认值）
*/

/*管理员-增加*/
function admin_add(title, url, w, h) {
    layer_show(title, url, w, h);
}

/*管理员-删除*/
function admin_del(obj, id) {
    layer.confirm('确认要删除吗？', function (index) {
        //此处请求后台程序，下方是成功后的前台处理……

        $(obj).parents("tr").remove();
        layer.msg('已删除!', {icon: 1, time: 1000});
    });
}

/*管理员-编辑*/
function admin_edit(title, url, id, w, h) {
    layer_show(title, url, w, h);
}
