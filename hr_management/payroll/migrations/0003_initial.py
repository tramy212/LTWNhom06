# Generated by Django 4.2.21 on 2025-05-20 03:42

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0002_initial'),
        ('payroll', '0002_auto_20250520_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Tên bảng lương')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mã bảng lương')),
                ('month', models.IntegerField(default=5, verbose_name='Tháng')),
                ('year', models.IntegerField(default=2025, verbose_name='Năm')),
                ('status', models.CharField(choices=[('draft', 'Nháp'), ('processing', 'Đang xử lý'), ('approved', 'Đã duyệt'), ('paid', 'Đã thanh toán')], default='draft', max_length=20, verbose_name='Trạng thái')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')),
                ('attendance_summary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payrolls', to='attendance.attendancesummary', verbose_name='Bảng chấm công')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_payrolls', to=settings.AUTH_USER_MODEL, verbose_name='Người tạo')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.position', verbose_name='Vị trí')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bảng lương',
                'verbose_name_plural': 'Bảng lương',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PayrollDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='Lương cơ bản')),
                ('attendance_ratio', models.DecimalField(decimal_places=4, default=Decimal('1.0000'), max_digits=5, verbose_name='Tỷ lệ hưởng lương')),
                ('standard_workdays', models.FloatField(default=0.0, verbose_name='Số công chuẩn')),
                ('actual_workdays', models.FloatField(default=0.0, verbose_name='Số công thực tế')),
                ('unpaid_leave', models.FloatField(default=0.0, verbose_name='Số ngày nghỉ không lương')),
                ('reward_amount', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='Tiền thưởng')),
                ('discipline_amount', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='Tiền phạt')),
                ('gross_salary', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='Tổng thu nhập')),
                ('deduction_amount', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='Tổng khấu trừ')),
                ('net_salary', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='Thực lĩnh')),
                ('income_tax', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='Thuế TNCN')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Ghi chú')),
                ('deduction_data', models.JSONField(blank=True, default=dict, null=True, verbose_name='Dữ liệu khấu trừ')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee', verbose_name='Nhân viên')),
                ('payroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='payroll.payroll', verbose_name='Bảng lương')),
            ],
            options={
                'verbose_name': 'Chi tiết lương',
                'verbose_name_plural': 'Chi tiết lương',
                'unique_together': {('payroll', 'employee')},
            },
        ),
        migrations.CreateModel(
            name='PayrollDeduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên khấu trừ')),
                ('amount', models.FloatField(default=0.0, verbose_name='Giá trị')),
                ('is_percentage', models.BooleanField(default=False, verbose_name='Là phần trăm')),
                ('value', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='Số tiền')),
                ('payroll_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deductions', to='payroll.payrolldetail', verbose_name='Chi tiết lương')),
            ],
            options={
                'verbose_name': 'Khấu trừ lương',
                'verbose_name_plural': 'Khấu trừ lương',
            },
        ),
        migrations.CreateModel(
            name='PayrollAllowance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên phụ cấp')),
                ('amount', models.FloatField(default=0.0, verbose_name='Giá trị')),
                ('is_percentage', models.BooleanField(default=False, verbose_name='Là phần trăm')),
                ('value', models.DecimalField(decimal_places=0, default=0, max_digits=12, verbose_name='Số tiền')),
                ('payroll_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowances', to='payroll.payrolldetail', verbose_name='Chi tiết lương')),
            ],
            options={
                'verbose_name': 'Phụ cấp',
                'verbose_name_plural': 'Phụ cấp',
            },
        ),
    ]
