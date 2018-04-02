var dialog = {
    //错误弹出
    error:function (message) {
        layer.open({
            content:message,
            icon:2,
            title:"有问题发生了！",
            yes:function () {
                window.parent.parent.location.reload();
            }
        });
    },
    error_reload:function (message) {
        layer.open({
            content:message,
            icon:2,
            title:"有问提发生！",
            yes:function () {
                window.parent.parent.location.reload();
            }
        });
    },
    //成功弹出层
    success:function (message) {
        layer.open({
            content:message,
            icon:1,
            title:"成功！",
            yes:function () {
                window.parent.parent.location.reload();
            }
        });
    },
    //确认弹出层
    confirm:function (message) {
        layer.open({
            content:message,
            icon:3,
            bth:['是','否'],
            yes:function () {
                window.parent.parent.location.reload();
            }
        });
    },
    //无需跳转到指定页面的确认弹出层
    toconfirm:function (message) {
        layer.open({
            content:message,
            icon:3,
            btn:['确定']
        });
    }
};