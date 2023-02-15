# Домашнее задание к занятию "11.Teamcity"

## Подготовка к выполнению

1. В Ya.Cloud создайте новый инстанс (4CPU4RAM) на основе образа `jetbrains/teamcity-server`
2. Дождитесь запуска teamcity, выполните первоначальную настройку
3. Создайте ещё один инстанс(2CPU4RAM) на основе образа `jetbrains/teamcity-agent`. Пропишите к нему переменную окружения `SERVER_URL: "http://158.160.29.79:8111"`
<img width="1264" alt="image" src="https://user-images.githubusercontent.com/103331839/219116697-7b29bfd0-c0f1-43e5-9607-3ada57bb3791.png">


4. Авторизуйте агент
<img width="1255" alt="image" src="https://user-images.githubusercontent.com/103331839/219116920-a502fd86-cd59-4473-a8ad-efc568ad029c.png">


5. Сделайте fork [репозитория](https://github.com/aragastmatb/example-teamcity)
<img width="1356" alt="image" src="https://user-images.githubusercontent.com/103331839/219117504-a49c6ad4-fb6b-4009-bc76-9146d8a80fc7.png">


6. Создать VM (2CPU4RAM) и запустить [playbook](./infrastructure)
<img width="1269" alt="image" src="https://user-images.githubusercontent.com/103331839/219118331-3c520d91-1b01-41d8-8d52-c64509670dec.png">
<img width="1231" alt="image" src="https://user-images.githubusercontent.com/103331839/219120374-6b470ade-bdb3-4dd1-b543-65148f680aef.png">



## Основная часть

1-3. Создайте новый проект в teamcity на основе fork. Сделайте autodetect конфигурации. Сохраните необходимые шаги, запустите первую сборку master'a.
<img width="1098" alt="image" src="https://user-images.githubusercontent.com/103331839/219120992-92a9fa89-42d7-4849-a275-51c74bed09af.png">
<img width="878" alt="image" src="https://user-images.githubusercontent.com/103331839/219121472-49c2f468-21db-4753-b5bb-7b592a8a757f.png">
<img width="1401" alt="image" src="https://user-images.githubusercontent.com/103331839/219121606-bfc53167-2561-4399-bd44-3c74559869a8.png">
<img width="1297" alt="image" src="https://user-images.githubusercontent.com/103331839/219121703-8fd9cff5-2504-4aa3-9f29-d9bf102bbdc5.png">
<img width="1104" alt="image" src="https://user-images.githubusercontent.com/103331839/219124068-5cb3c256-dff5-4ee5-85a4-b2b2a4f8068c.png">
<img width="1098" alt="image" src="https://user-images.githubusercontent.com/103331839/219124264-9e56adb9-fbac-4cfe-b12e-98ac58521b0c.png">


4. Поменяйте условия сборки: если сборка по ветке `master`, то должен происходит `mvn clean deploy`, иначе `mvn clean test`
<img width="1404" alt="image" src="https://user-images.githubusercontent.com/103331839/219126474-9b3e0746-35cc-4546-ae58-ba61f89613d4.png">


7. Для deploy будет необходимо загрузить [settings.xml](./teamcity/settings.xml) в набор конфигураций maven у teamcity, предварительно записав туда креды для подключения к nexus
8. В pom.xml необходимо поменять ссылки на репозиторий и nexus
9. Запустите сборку по master, убедитесь что всё прошло успешно, артефакт появился в nexus
10. Мигрируйте `build configuration` в репозиторий
11. Создайте отдельную ветку `feature/add_reply` в репозитории
12. Напишите новый метод для класса Welcomer: метод должен возвращать произвольную реплику, содержащую слово `hunter`
13. Дополните тест для нового метода на поиск слова `hunter` в новой реплике
14. Сделайте push всех изменений в новую ветку в репозиторий
15. Убедитесь что сборка самостоятельно запустилась, тесты прошли успешно
16. Внесите изменения из произвольной ветки `feature/add_reply` в `master` через `Merge`
17. Убедитесь, что нет собранного артефакта в сборке по ветке `master`
18. Настройте конфигурацию так, чтобы она собирала `.jar` в артефакты сборки
19. Проведите повторную сборку мастера, убедитесь, что сбора прошла успешно и артефакты собраны
20. Проверьте, что конфигурация в репозитории содержит все настройки конфигурации из teamcity
21. В ответ предоставьте ссылку на репозиторий

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
