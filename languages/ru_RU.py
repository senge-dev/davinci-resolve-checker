local_str = {
    "locale": "Использую локаль",
    "project name": "DaVinci Resolve checker",
    "you are running": "Вы используете",
    "script not tested on distro": "но этот скрипт не был протестирован на нём.",
    "which DR package": "Установленный пакет DaVinci Resolve:",
    "chassis": "Тип компьютера:",
    "unsupported chassis": "Предупреждение: ваш тип компьютера не поддерживается скриптом. Сообщите, пожалуйста, о вашем случае.",
    "Notebook": "ноутбук",
    "Laptop": "лэптоп",
    "Desktop": "десктоп",
    "openCL drivers": "Установленные OpenCL драйвера:",
    "presented gpus": "Представленные GPU:",
    "kernel driver": "используемый драйвер:",
    "opengl vendor": "Строка поставщика OpenGL:",
    "missing opengl vendor": "Не смог определить строку поставщика OpenGL. Возможно, вы пытаетесь использовать AMD Pro OpenGL, в то время как у вас первичный GPU Intel. Также, возможно, вы запускаете этот скрипт через ssh.",
    "should uninstall opencl-mesa": "Вам нужно удалить opencl-mesa. Иначе DR (v17.1.1) ведёт себя неправильно: изображение повреждено. Но если вы снимите галочку gpu в настройках и перезапустите DR, тогда вся сессия рабочего стола станет повреждённой и вам останется только перезагрузить компьютер. По крайней мере такое поведение замечено на amd gpu.",
    "several intel gpus": "У вас несколько видеокарт INTEL. Это странно. У вас многопроцессорная десктопная матплата? Или вы используете встроенную и дискретную видеокарту от intel (не существует на момент написания)?",
    "several amd gpus": "У вас несколько видеокарт AMD. DR Studio может использовать несколько GPU. Скрипт проверит используется ли соответствующий драйвер для рендерящего GPU. Но имейте в виду, что если вы используете prime offloading, основному GPU по-прежнему нужен соответствующий драйвер (скрипт это не проверяет).",
    "several nvidia gpus": "У вас несколько видеокарт NVIDIA. Это странно. Какую вы собираетесь использовать?",
    "confused by nvidia and amd gpus": "У вас есть видеокарта как от AMD, так и от NVIDIA. Это странно. Какую вы собираетесь использовать?",
    "only intel gpu, cannot run DR": "У вас есть только видеокарта от Intel. На данный момент DR не умеет использовать intel видеокарты для OpenCL. Вы не сможете запустить DR. См. https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=81579",
    "mixed intel and amd gpus": "Мне не удалось найти работающую конфигурацию на ноутбуках для Intel + AMD графики. А вам?",
    "set primary display to PCIE": "Ваша основная видеокарта - Intel. Перейдите в настройки uefi и назначьте первичную видеокарту на PCIE. Иначе вы не сможете использовать DaVinci Resolve (я это не тестировал).",
    "switch from radeon driver to amdgpu": "Вы сейчас используете драйвер radeon. Переключитесь на amdgpu, как описано тут: https://wiki.archlinux.org/title/AMDGPU#Enable_Southern_Islands_(SI)_and_Sea_Islands_(CIK)_support. Иначе вы не сможете запустить DaVinci Resolve.",
    "no support for amd driver, cannot run DR": "Ваша видеокарта поддерживает лишь драйвер radeon. Для DaVinci Resolve нужен проприетарный драйвер amdgpu progl, который работает поверх драйвера amdgpu. Вы не сможете запустить DaVinci Resolve.",
    "not running amdgpu driver, cannot run DR": "Почему-то вы не используете amdgpu драйвер. Вы не сможете запустить DaVinci Resolve.",
    "not using Pro OpenGL": "Вы не используете Pro OpenGL реализацию. Установите amdgpu-pro-libgl и запустите DaVinci Resolve, используя префикс progl. Иначе он аварийно завершится.",
    "missing opencl driver": "У вас не установлен opencl-driver для видеокарты AMD. Установите его, иначе вы не сможете использовать DaVinci Resolve.",
    "good to run DR": "Всё выглядит хорошо. У вас должно получиться нормально запустить DaVinci Resolve.",
    "missing opencl-nvidia package": "У вас нет пакета opencl-nvidia (либо альтернативного пакета, предоставляющего opencl-nvidia). Установите его, иначе вы не сможете использовать DR. Даже если вы планируете использовать cuda, opencl-nvidia всё равно установится как его зависимость.",
    "missing nvidia as kernel driver": "Вы не используете nvidia драйвер. Используйте проприетарный nvidia драйвер, иначе вы не сможете использовать DaVinci Resolve.",
    "not running nvidia rendered": "Вы не используете рендерер NVIDIA. Попробуйте запустить скрипт через prime-run или каким-то другим способом для optimus, иначе вы не сможете использовать DaVinci Resolve.",
    "opencl-amd and progl versions mismatch": "Внимание: версии opencl-amd (%s) и amdgpu-pro-libgl (%s) не совпадают.",
    "skipping vfio binded gpu": "GPU %s использует драйвер vfio-pci, убираем его из дальнейших проверок.",
    "amd codename undetectable": "Внимание: ваш gpu не найден в списке кодовых имен. Предполагаем что это старый GPU, требующий progl. Если это не так, пожалуйста сообщите.",
}
