from sqlalchemy import Column, Integer, String, Date, Boolean, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db
from flask_login import UserMixin
from enum import Enum as UserEnum


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class SaleBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class TaiKhoan(SaleBase, UserMixin):
    __tablename__ = "user"
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    active = Column(Boolean, default=True)

    nhanvien = relationship('NhanVien', backref='user', lazy=True)


class NhanVien(db.Model):
    __tablename__ = "nhanvien"
    maNhanVien = Column(Integer, primary_key=True, autoincrement=True)
    hoTen = Column(String(50), nullable=False)
    gioiTinh = Column(String(50), nullable=False)
    ngaySinh = Column(Date, nullable=False)
    diaChi = Column(String(50), nullable=False)
    id = Column(Integer, ForeignKey(TaiKhoan.id), nullable=False)
    contact = Column(String(50), nullable=False)


class Thuoc(db.Model):
    __tablename__ = "thuoc"
    maThuoc = Column(Integer, primary_key=True, autoincrement=True)
    tenThuoc = Column(String(50), nullable=False)
    moTa = Column(String(50), nullable=True)
    giaTien = Column(Float, default=0)
    chitiethoadon = relationship('ChiTietHoaDon', backref='thuoc', lazy=True)

    # hinhAnh = Column(String(50), nullable=True)


class KhamBenh(db.Model):
    __tablename__ = "danhsachkhambenh"
    maKB = Column(Integer, primary_key=True, autoincrement=True)
    hoTen = Column(String(50), nullable=False)
    gioiTinh = Column(String(50), nullable=False)
    ngaySinh = Column(Date)
    diaChi = Column(String(50), nullable=False)


class BenhNhan(db.Model):
    __tablename__ = "danhsachbenhnhan"
    maBN = Column(Integer, primary_key=True, autoincrement=True)
    hoTen = Column(String(50), nullable=False)
    ngayKham = Column(Date)
    loaiBenh = Column(String(50), nullable=False)
    trieuchung = Column(String(50), nullable=False)
    phieukhambenh = relationship('PhieuKhamBenh', backref='danhsachbenhnhan', lazy=True)


class PhieuKhamBenh(db.Model):
    __tablename__ = "phieukhambenh"
    maPKB = Column(Integer, primary_key=True, autoincrement=True)
    hoTen = Column(String(50), nullable=False)
    ngayKham = Column(Date)
    trieuchung = Column(String(50), nullable=False)
    tenThuoc = Column(String(50), nullable=False)
    soLuong = Column(Integer)
    cachDung = Column(String(50), nullable=False)
    maBN = Column(Integer, ForeignKey(BenhNhan.maBN), nullable=False)
    hoadon = relationship('HoaDon', backref='phieukhambenh', lazy=True)
    chitiethoadon = relationship('ChiTietHoaDon', backref='phieukhambenh', lazy=True)


class HoaDon(db.Model):
    __tablename__ = "hoadon"
    maHoaDon = Column(Integer, primary_key=True, autoincrement=True)
    ngayBan = Column(Date)
    tienThuoc = Column(Float, default=0)
    tienKham = Column(Float, default=0)
    maPKB = Column(Integer, ForeignKey(PhieuKhamBenh.maPKB), nullable=False)


class ChiTietHoaDon(db.Model):
    __tablename__ = "chitiethoadon"
    maPKB = Column(Integer, ForeignKey(PhieuKhamBenh.maPKB), primary_key=True)
    maThuoc = Column(Integer, ForeignKey(Thuoc.maThuoc), primary_key=True)
    soLuong = Column(Integer)
    cachDung = Column(String(50), nullable=False)



if __name__ == "__main__":
    db.create_all()
