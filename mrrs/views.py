from django.http.response import HttpResponse
from django.shortcuts import render
from .models import room_reservation
from . import forms
def mrrs(request):
    """
    会議室予約システム画面の関数
    """
    # リクエストがPOST形式の場合 データーベースに会議室予約システムの情報を登録する.
    if request.method == "POST":
        # 予約ID
        reserve_id = request.POST.get('reserve_id')
        # 会議室ID
        room_id = request.POST.get('room_id')
        # 利用者
        reserve_name = request.POST.get('reserve_name')
        # 開始日時
        start_date_time = request.POST.get('start_date_time')
        # 終了日時
        end_date_time = request.POST.get('end_date_time')  
        # リクエストパラメーターをデーターモデルに当て込みます.
        data_object = room_reservation(
            id=reserve_id, 
            room_id=room_id, 
            user=reserve_name, 
            start_date_time=start_date_time, 
            end_date_time=end_date_time, 
            del_flg=0)
        # データーを登録する.
        data_object.save()
    # データーモデルからデーターを取得する.
    reserv_data = room_reservation.objects.all()
    # フォームオブジェクトを取得する.
    form = forms.reserve_room(request.GET or None)
    # テンプレートに渡す値を設定する
    display = {
        'form': form,
        'reserve_data' : reserv_data,
    }
    return render(request, 'resurve.html', display)