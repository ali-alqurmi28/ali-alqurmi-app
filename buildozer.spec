[app]
title = علي القورمي
package.name = alialqurmiapp
package.domain = org.alialqurmi

source.dir =.
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0
requirements = python3,kivy,android,openssl

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk_path = 
android.ndk_path =
